# default_constants.py

- `SUB_SLOT_ITERS_STARTING` ~= `vdf_speed` * `SUB_SLOT_TIME_TARGET`
- `DIFFICULTY_CONSTANT_FACTOR`
- `DIFFICULTY_STARTING`
- `NUMBER_ZERO_BITS_PLOT_FILTER`
- `MIN_PLOT_SIZE`

```python
from chia.consensus.pos_quality import _expected_plot_size

# ~= number of plots
DIFFICULTY_CONSTANT_FACTOR * DIFFICULTY_STARTING / (
    SUB_SLOT_ITERS_STARTING // NUM_SPS_SUB_SLOT * _expected_plot_size(k)) * (
    1 << NUMBER_ZERO_BITS_PLOT_FILTER)
```

# initial-config.yaml

- `GENESIS_PRE_FARM_POOL_PUZZLE_HASH`
- `GENESIS_PRE_FARM_FARMER_PUZZLE_HASH`

[Address and puzzle hash converter](https://www.chiaexplorer.com/tools/address-puzzlehash-converter)
