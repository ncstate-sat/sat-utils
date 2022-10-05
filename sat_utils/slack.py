from slack_sdk import WebClient


class Slack:
    """
    Upload files directly to our Slack channels using this shared utility class.
    """

    def __init__(self, token):
        self.client = WebClient(token=token)

    def upload_file(self, channel, file_path, file_name, file_type, title, initial_comment):
        """
        Upload a file to Slack.
        """
        try:
            self.client.files_upload(
                channels=channel,
                file=file_path,
                filename=file_name,
                filetype=file_type,
                title=title,
                initial_comment=initial_comment
            )
        except Exception as e:
            print("Slack encountered an error: {}".format(e))
