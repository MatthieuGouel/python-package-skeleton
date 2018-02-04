"""Initialization module of the package."""
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('skeleton').version
except pkg_resources.DistributionNotFound:  # pragma: no cover
    __version__ = "Not installed"

__all__ = ()
