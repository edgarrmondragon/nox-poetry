"""Type stubs for nox_poetry.sessions."""
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import TypeVar
from typing import Union

import nox.sessions
import nox.virtualenv

Python = Optional[Union[str, Sequence[str], bool]]

class _PoetrySession:
    def install(self, *args: str, **kwargs: Any) -> None: ...
    def installroot(
        self, *, distribution_format: str = ..., extras: Iterable[str] = ...
    ) -> None: ...
    def export_requirements(self) -> Path: ...
    def build_package(self, *, distribution_format: str = ...) -> str: ...

class Session:
    poetry: _PoetrySession
    _session: nox.Session
    _runner: nox.sessions.SessionRunner
    def __init__(self, session: nox.Session) -> None: ...
    def install(self, *args: str, **kwargs: Any) -> None: ...
    @property
    def env(self) -> Dict[str, str]: ...
    @property
    def posargs(self) -> List[str]: ...
    @property
    def virtualenv(self) -> nox.virtualenv.ProcessEnv: ...
    @property
    def python(self) -> Python: ...
    @property
    def bin_paths(self) -> Optional[List[str]]: ...
    @property
    def bin(self) -> Optional[str]: ...
    def create_tmp(self) -> str: ...
    @property
    def interactive(self) -> bool: ...
    def chdir(self, dir: str) -> None: ...
    def cd(self, dir: str) -> None: ...
    def run(
        self, *args: str, env: Optional[Mapping[str, str]] = ..., **kwargs: Any
    ) -> Optional[Any]: ...
    def run_always(
        self, *args: str, env: Optional[Mapping[str, str]] = ..., **kwargs: Any
    ) -> Optional[Any]: ...
    def conda_install(
        self, *args: str, auto_offline: bool = ..., **kwargs: Any
    ) -> None: ...
    def notify(self, target: Union[str, nox.sessions.SessionRunner]) -> None: ...
    def log(self, *args: Any, **kwargs: Any) -> None: ...
    def error(self, *args: Any) -> NoReturn: ...
    def skip(self, *args: Any) -> NoReturn: ...

SessionFunction = Callable[..., None]
SessionDecorator = Callable[[SessionFunction], SessionFunction]
@overload
def session(__func: SessionFunction) -> SessionFunction: ...
@overload
def session(
    __func: None = ...,
    python: Python = ...,
    py: Python = ...,
    reuse_venv: Optional[bool] = ...,
    name: Optional[str] = ...,
    venv_backend: Any = ...,
    venv_params: Any = ...,
) -> SessionDecorator: ...
