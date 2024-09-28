import bpy
import random

# Function to display the chatbot message
class MentalHealthChatbotPanel(bpy.types.Panel):
    bl_label = "Mental Health Chatbot"
    bl_idname = "PT_MentalHealthChatbotPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Chatbot'
    
    # Draw the chatbot UI in the Blender 3D Viewport
    def draw(self, context):
        layout = self.layout

        # Add a button for starting the chatbot conversation
        row = layout.row()
        row.operator("wm.start_chatbot", text="Start Chatbot")

# Operator for chatbot interaction
class StartChatbotOperator(bpy.types.Operator):
    bl_idname = "wm.start_chatbot"
    bl_label = "Start Mental Health Chatbot"
    
    # Execute the chatbot logic when the operator is triggered
    def execute(self, context):
        self.chatbot_logic()
        return {'FINISHED'}
    
    def chatbot_logic(self):
        welcome_message()
        while True:
            mood = mood_check_in()
            if not self.handle_mood(mood):
                break
    
    # Print the chatbot logic in Blender's console
    def handle_mood(self, mood):
        if mood == 'happy':
            gratitude_journal()
        elif mood in ['anxious', 'stressed', 'nervous']:
            cognitive_restructuring()
        elif mood in ['sad', 'down', 'depressed']:
            behavioral_activation()
        else:
            return False
        
        another_exercise = input("Would you like to try another exercise? (yes or no): ").lower()
        return another_exercise == 'yes'

# Welcome message
def welcome_message():
    print("Hello, I'm your mental health chatbot. I’m here to help you reflect on your thoughts and feelings.")
    print("We'll work through some exercises based on Cognitive Behavioral Therapy (CBT).")
    print("Remember, I’m not a replacement for a therapist, but I can help you reflect and think through your feelings.")
    print("\nLet's get started!\n")

# Check in on the user's mood
def mood_check_in():
    print("How are you feeling today? (e.g., happy, anxious, sad, stressed, etc.)")
    mood = input("Your mood: ").lower()
    return mood

# Cognitive Restructuring: Identifying and challenging negative thought patterns
def cognitive_restructuring():
    print("\n--- Cognitive Restructuring ---")
    print("This exercise will help you challenge negative thoughts and reframe them in a more positive way.\n")

    thought = input("Can you share a negative thought or worry you're having right now? ")
    
    print("\nNow, let's break it down.")
    print("1. What evidence do you have that this thought is true?")
    evidence_for = input("Evidence for: ")

    print("2. What evidence do you have that this thought is not true?")
    evidence_against = input("Evidence against: ")

    print("\nLet's reframe that thought.")
    print("Given the evidence you’ve shared, how could you rephrase that thought to be more balanced and realistic?")
    new_thought = input("New balanced thought: ")
    
    print(f"\nGreat work! Here's your new balanced thought: '{new_thought}'")
    encouragement()

# Behavioral Activation: Encouraging positive activities to improve mood
def behavioral_activation():
    print("\n--- Behavioral Activation ---")
    print("This exercise will help you identify some positive activities that could help improve your mood.\n")
    
    activities = [
        "Go for a walk outside.",
        "Read a book you enjoy.",
        "Listen to your favorite music.",
        "Do some gentle stretching or yoga.",
        "Call or text a friend.",
        "Take a few minutes to meditate or breathe deeply."
    ]
    
    print("Here are some activities you could try to boost your mood:\n")
    for i, activity in enumerate(activities, 1):
        print(f"{i}. {activity}")
    
    chosen_activity = input("\nWhich activity sounds good to you? (or type your own): ")
    
    print(f"\nThat's a great choice! Doing something positive, even if it's small, can make a big difference.")
    encouragement()

# Gratitude Journaling: Encouraging positive reflection
def gratitude_journal():
    print("\n--- Gratitude Journaling ---")
    print("Gratitude is a great way to remind ourselves of the good things in life.\n")
    
    gratitude_1 = input("What's one thing you're grateful for today? ")
    gratitude_2 = input("Can you think of another thing you're grateful for? ")
    gratitude_3 = input("One more thing you're thankful for? ")
    
    print("\nThank you for sharing!")
    print(f"Here are three things you're grateful for: {gratitude_1}, {gratitude_2}, and {gratitude_3}.")
    encouragement()

# Encouragement messages after exercises
def encouragement():
    messages = [
        "You're doing a great job. Keep reflecting and working on yourself!",
        "Small steps add up to big changes. Stay positive!",
        "You're capable of managing these feelings. Keep going!",
        "You're not alone in this. It's okay to feel what you're feeling.",
        "Remember, progress is progress, no matter how small. Keep up the good work!"
    ]
    print(random.choice(messages))
    print("\n")

# Register the chatbot in Blender's UI
def register():
    bpy.utils.register_class(MentalHealthChatbotPanel)
    bpy.utils.register_class(StartChatbotOperator)

def unregister():
    bpy.utils.unregister_class(MentalHealthChatbotPanel)
    bpy.utils.unregister_class(StartChatbotOperator)

if __name__ == "__main__":
    register()