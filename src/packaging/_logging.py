# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.
from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logging import Logger


@lru_cache(maxsize=None)
def get_logger(name: str) -> Logger:
    import logging

    return logging.getLogger(name)
