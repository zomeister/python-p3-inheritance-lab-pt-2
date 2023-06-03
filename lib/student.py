class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
        pass
    def raise_hand(self):
        print("Pick me!")
        pass
    pass

class ChattyStudent(Student):
    def hello(self):
        super(ChattyStudent, self).hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    def raise_hand(self):
        for _ in range(10):
            super(ChattyStudent, self).raise_hand()
    
        pass
    pass
