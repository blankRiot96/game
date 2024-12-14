import functools
import inspect
from collections.abc import Callable
from typing import Any

from loguru import logger

from src.entities import EntityType


@functools.lru_cache
def get_required_components(func: Callable) -> list[str]:
    return list(inspect.signature(func).parameters)


def process(
    components: dict[str, list[Any]],
    processes: dict[int, list[Callable]],
):

    for component_index, process_list in processes.items():
        for process in process_list:
            components_required = get_required_components(process)
            process_arguments = {
                component_name: components[component_name][component_index]
                for component_name in components_required
            }
            modified_components = process(**process_arguments)

            if modified_components is None:
                continue

            for component_name, modified_component in zip(
                components_required, modified_components
            ):
                components[component_name][component_index] = modified_component


def add_process(
    processes: dict[int, list[Callable]],
    entities: list[EntityType],
    entity_indeces: dict[EntityType, int],
    callback: Callable,
) -> None:
    for entity_type in entities:
        processes[entity_indeces.get(entity_type)].append(callback)

    logger.debug(f"Added Process `{callback.__name__}`")
