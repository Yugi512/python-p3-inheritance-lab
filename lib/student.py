#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self,knowledge):
        super().__init__(self.first_name,self.last_name)
        self.knowledge.append(knowledge)