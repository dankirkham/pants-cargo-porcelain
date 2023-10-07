from . import subsystems
from . import target_types as tt
from .goals import fmt, package, tailor, test
from .internal import build
from .util_rules import cargo, rustup


def rules():
    return [
        *subsystems.rules(),
        *tailor.rules(),
        #        *package.rules(),
        *rustup.rules(),
        *tt.rules(),
        *cargo.rules(),
        *build.rules(),
        *package.rules(),
        *fmt.rules(),
        *test.rules(),
    ]


def target_types():
    return tt.target_types()
