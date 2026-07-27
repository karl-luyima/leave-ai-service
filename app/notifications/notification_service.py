import logging


logger = logging.getLogger(__name__)


class NotificationService:


    def send_notification(
        self,
        employee,
        message
    ):

        # Later:
        # - Email API
        # - SMS API
        # - CheckinPro notification API


        logger.info(
            f"Notification sent to {employee}: {message}"
        )


        return {
            "employee": employee,
            "status": "sent",
            "message": message
        }