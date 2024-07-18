from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class PrimeChecker(App):

    def build(self):
        self.title = 'Prime Number Checker'
        self.layout = BoxLayout(orientation='vertical', padding=10)

        self.input_label = Label(text='Enter a number:')
        self.layout.add_widget(self.input_label)

        self.input_number = TextInput(multiline=False)
        self.layout.add_widget(self.input_number)

        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

        check_button = Button(text='Check Prime', on_press=self.check_prime)
        self.layout.add_widget(check_button)

        return self.layout

    def is_prime(self, n):
        """ Check if a number is prime """
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def check_prime(self, instance):
        try:
            num = int(self.input_number.text)
            if self.is_prime(num):
                self.result_label.text = f'{num} is a prime number.'
            else:
                self.result_label.text = f'{num} is not a prime number.'
        except ValueError:
            self.result_label.text = 'Please enter a valid integer.'

if __name__ == '__main__':
    PrimeChecker().run()
