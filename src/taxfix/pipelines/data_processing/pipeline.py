from kedro.pipeline import Pipeline, node, pipeline

from .nodes import split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs="dataset",
                outputs=["train_dataset", "inference_dataset"],
                name="split_dataset_into_train_and_inference_node",
            ),
        ]
    )
