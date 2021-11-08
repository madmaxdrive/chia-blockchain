from chia.util.config import _constants
from chia.util.ints import uint32, uint64

# 1 Chia coin = 1,000,000,000,000 = 1 trillion mojo.
# _mojo_per_chia = 1000000000000
_blocks_per_year = 1681920  # 32 * 6 * 24 * 365

_block_rewards = _constants()["block_rewards"]


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    return uint64(int((7 / 8) * calculate_reward(height)))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    return uint64(int((1 / 8) * calculate_reward(height)))


def calculate_reward(height: uint32):
    if height == 0 and _block_rewards["prefarm"] is not None:
        return _block_rewards["prefarm"]

    y = 12 * height // _blocks_per_year
    p = 0
    for i, t in reversed(_block_rewards["half_life"].items()):
        if i < y:
            p += (y - i) // t
            y = i

    return _block_rewards["initial"] / (2 ** p)
