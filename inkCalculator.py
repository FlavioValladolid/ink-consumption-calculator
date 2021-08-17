
class Calculator:
    def __init__(self,label_width,label_length,total_labels,percent_ink_transfer,percent_ink_coverage,anilox_volume):
        self.label_width = label_width
        self.label_length = label_length
        self.total_labels = total_labels
        self.percent_ink_transfer = percent_ink_transfer
        self.percent_ink_coverage = percent_ink_coverage
        self.anilox_volume = anilox_volume

    def TotalInk(self):
        return self.label_width*self.label_length*self.total_labels*self.percent_ink_transfer*self.percent_ink_coverage*self.anilox_volume/10000*0.0000002641721
    
print(Calculator(10,16.25,1000,75,18.03,4).TotalInk())

