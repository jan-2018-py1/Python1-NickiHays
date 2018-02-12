class Call(object):
    def __init__(self, call_id, name, phone_number, time, reason):
        self.call_id = call_id
        self.name = name
        self.phone_number = phone_number
        self.reason = reason
        self.time = time
    def display(self):
        print 'Unique ID:', self.call_id
        print 'Caller Name:', self.name
        print 'Caller Phone Number:', self.phone_number
        print 'Call Time:', self.time
        print 'Call Reason:', self.reason

class CallCenter(Call):
    def __init__(self):
        self.queue_len = 0
        self.callers = []
    
    def add(self, call_id, name, phone_number, time, reason):
        caller_list = Call(call_id, name, phone_number, time, reason)
        self.callers.append(caller_list)
        self.queue_len += 1
        return self
    
    def remove(self):
        self.callers.pop(0)
        self.queue_len -= 1
        return self
    
    def remove_number(self, phone_number):
        for caller in range(len(self.callers)):
            if self.callers[caller].phone_number == phone_number:
                removex = self.callers.index(self.callers[caller])
        self.callers.pop(removex)
        self.queue_len -= 1
        return self

    def info(self):
        print 'Queue order:'
        for caller in range(len(self.callers)):
            print self.callers[caller].name
            print self.callers[caller].phone_number
            print "Queue length:", self.queue_len
        return self


b = CallCenter()
#b.add(1,'James', '555-7777', '12:30', 'IT assistance').add(2,'Nicki', '555-7778', '12:45', 'order help').remove().info()
b.add(1,'James', '555-7777', '12:30', 'IT assistance').add(2,'Nicki', '555-7778', '12:45', 'order help').remove_number('555-7778').info()




