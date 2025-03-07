from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model, run_inference


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["train_dataset", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train", "params:model_parameters"],
                outputs="model",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["model", "X_test", "y_test"],
                name="evaluate_model_node",
                outputs=None,
            ),
            node(
                func=run_inference,
                inputs=["model", "inference_dataset", "params:model_options"],
                name="run_inference_node",
                outputs="inference_results",
            ),
        ]
    )
