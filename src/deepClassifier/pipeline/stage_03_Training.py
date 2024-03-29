from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallBacks, Training
from deepClassifier import logger

STAGE_NAME = "Training"
def main():
    config = ConfigurationManager()
    prepare_callbacks_config = config.get_prepare_callback_config(),
    prepare_callbacks = PrepareCallBacks(Config=prepare_callbacks_config),
    callback_list = prepare_callbacks.get_tb_callbacks()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    
    
    
    
    
    
    
    
    
    
    
    prepare_callbacks_config = config.get_prepare_callback_config(),
    prepare_callbacks = PrepareBaseModel(Config=prepare_callbacks_config),
    callback_list = prepare_callbacks.get_tb_callbacks()