class AbstractHelloWorldBuilder:
    def build(self):
        raise NotImplementedError("Subclasses must implement this method.")

class HelloWorldBuilder(AbstractHelloWorldBuilder):
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def build(self):
        return "".join(self.parts)

class Cipher:
    @staticmethod
    def encode(text, shift):
        return "".join(
            chr((ord(char) - 32 + shift) % 95 + 32) if 32 <= ord(char) <= 126 else char
            for char in text
        )

    @staticmethod
    def decode(text, shift):
        return "".join(
            chr((ord(char) - 32 - shift) % 95 + 32) if 32 <= ord(char) <= 126 else char
            for char in text
        )

class QuantumHelloWorldGenerator:
    def __init__(self, state="superposition"):
        self.state = state

    def collapse_state(self):
        return "Hello" if self.state == "superposition" else "world"

class HelloWorldFactory:
    @staticmethod
    def create_hello_world():
        builder = HelloWorldBuilder()
        quantum_gen = QuantumHelloWorldGenerator()
        
        builder.add_part(quantum_gen.collapse_state())
        builder.add_part(" ")
        builder.add_part(Cipher.decode(Cipher.encode("world", 5), 5))
        
        return builder.build()

def main():
    import threading
    import queue

    def print_with_delay(q):
        while True:
            message = q.get()
            if message == "EXIT":
                break
            print(message)

    message_queue = queue.Queue()
    printer_thread = threading.Thread(target=print_with_delay, args=(message_queue,))
    printer_thread.start()

    message_queue.put(HelloWorldFactory.create_hello_world())
    message_queue.put("EXIT")
    printer_thread.join()

if __name__ == "__main__":
    main()