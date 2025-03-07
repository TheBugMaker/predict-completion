from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_diagram_data
)


def create_pipeline(**kwargs) -> Pipeline:
    """This is a simple pipeline which generates a pair of plots"""
    return pipeline(
        [
            node(
                func=generate_diagram_data,
                inputs="inference_results",
                outputs="diagram",
            ),
        ]
    )
