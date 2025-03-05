class messenger:
    def use_keyboard(self):
        print('using keyboard')

    def send_message(self):
        print('text message sent')

    def receive_message(self):
        print('text message received')


class whatsappmessenger(messenger):
    def send_message(self):
        print('Text,video and audio sent using WA')

    def receive_message(self):
        print('Text,video and audio received using WA ')

class facebookmessenger(messenger):
    def send_message(self):
        print('Text,video and audio sent using FM')

    def receive_message(self):
        print('Text,video and audio received using FM')

class instamessenger(messenger):
    def send_message(self):
        print('Text,video and audio are sent using insta')

    def receive_message(self):
        print('Text,video and audio are received using insta')


wa = whatsappmessenger()
fm = facebookmessenger()
im = instamessenger()

wa.use_keyboard()
wa.send_message()
wa.receive_message()

fm.use_keyboard()
fm.send_message()
fm.receive_message()

im.use_keyboard()
im.send_message()
im.receive_message()

#polymorphic code of the above program
class messenger:
    def use_keyboard(self):
        print('using keyboard')

    def send_message(self):
        print('text message sent')

    def receive_message(self):
        print('text message received')


class whatsappmessenger(messenger):
    def send_message(self):
        print('Text,video and audio sent using WA')

    def receive_message(self):
        print('Text,video and audio received using WA ')

class facebookmessenger(messenger):
    def send_message(self):
        print('Text,video and audio sent using FM')

    def receive_message(self):
        print('Text,video and audio received using FM')

class instamessenger(messenger):
    def send_message(self):
        print('Text,video and audio are sent using insta')

    def receive_message(self):
        print('Text,video and audio are received using insta')

def use_messenger(ref):
        ref.use_keyboard()
        ref.send_message()
        ref.receive_message()


wa = whatsappmessenger()
fm = facebookmessenger()
im = instamessenger()

use_messenger(wa)
use_messenger(fm)
use_messenger(im)


#simplified and specialized code using polymorphism and duck typing 
class messenger:
    def use_keyboard(self):
        print('using keyboard')

    def send_message(self):
        print('text message sent')

    def receive_message(self):
        print('text message received')


class whatsappmessenger(messenger):
    def send_message(self):
        print('Text,video and audio sent using WA')

    def receive_message(self):
        print('Text,video and audio received using WA ')

    def send_live_location(self):
        print('Live location is sent using wa')

class facebookmessenger(messenger):
    def send_message(self):
        print('Text,video and audio sent using FM')

    def receive_message(self):
        print('Text,video and audio received using FM')

    def use_builtin_apps(self):
        print('Built in apps are used in fm')

class instamessenger(messenger):
    def send_message(self):
        print('Text,video and audio are sent using insta')

    def receive_message(self):
        print('Text,video and audio are received using insta')

    def add_filters(self):
        print('filters are added in im')

def use_messenger(ref):
        ref.use_keyboard()
        ref.send_message()
        ref.receive_message()
        if type(ref) == whatsappmessenger: #duck typing
         ref.send_live_location()
        if type(ref) == facebookmessenger:  #duck typing
         ref.use_builtin_apps()
        if type(ref) == instamessenger:   #duck typing
         ref.add_filters()


wa = whatsappmessenger()
fm = facebookmessenger()
im = instamessenger()

use_messenger(wa)
use_messenger(fm)
use_messenger(im)