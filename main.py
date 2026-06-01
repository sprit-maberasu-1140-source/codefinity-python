from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        return f"Email sent: {message}"

class SMSNotifier(Notifier):
    def send(self, message):
        return f"SMS sent: {message}"

def notify_user(notifier, message):
    return notifier.send(message)

# Example usage (do not remove these lines):
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
print(notify_user(email_notifier, "Welcome!"))
print(notify_user(sms_notifier, "Your code is 1234."))