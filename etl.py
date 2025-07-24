from datetime import datetime
import sys

from loguru import logger
from prefect import flow
from prefect.states import Completed

from subflows import Extraction, Transform, Loading

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
log_filename = f"{datetime.now().strftime('%Y%m%d')}-update.log"
logger.add(log_filename, format="{time} {level} {message}", rotation="1 day")


@flow(name="main-flow")
def main():
    extract = Extraction("config.yaml")
    state = extract.run()  # type: ignore

    if not state.continue_run:
        return Completed(name="Skipped", message=state.message)

    logger.info("Extraction successfully completed!")

    transform = Transform("config.yaml", state.df)
    state = transform.run()  # type: ignore

    if not state.continue_run:
        return Completed(name="Skipped", message=state.message)

    logger.info("Transformation successfully completed!")

    load = Loading("config.yaml", state.df)
    state = load.run()  # type: ignore

    if not state.continue_run:
        return Completed(name="Skipped", message=state.message)

    logger.info("Flow Completed successfully!")
    return


if __name__ == "__main__":
    main()
