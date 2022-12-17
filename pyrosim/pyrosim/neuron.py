import math

import pybullet

import pyrosim as pyrosim

import constants as const

class NEURON:

    def __init__(self, line):
        self.Determine_Name(line)
        self.Determine_Type(line)
        self.Search_For_Link_Name(line)
        self.Search_For_Joint_Name(line)
        self.Set_Value(0.0)

    def Add_To_Value( self, value ):
        self.Set_Value( self.Get_Value() + value )

    def Get_Joint_Name(self):
        return self.jointName

    def Get_Link_Name(self):
        return self.linkName

    def Get_Name(self):
        return self.name

    def Get_Value(self):
        return self.value

    def Is_Sensor_Neuron(self):
        return self.type == const.SENSOR_NEURON

    def Is_Hidden_Neuron(self):
        return self.type == const.HIDDEN_NEURON

    def Is_Motor_Neuron(self):
        return self.type == const.MOTOR_NEURON

    def Print(self):
        # self.Print_Name()
        # self.Print_Type()
        self.Print_Value()
        # print("")

    def Set_Value(self, value):
        self.value = value

    def Update_Sensor_Neuron(self):
        self.Set_Value(
            pyrosim.Get_Touch_Sensor_Value_For_Link(self.Get_Link_Name())
        )

    def Update_Hidden_Or_Motor_Neuron(self, neurons, synapses):
        self.Set_Value(0.0)
        name = self.Get_Name()
        for sK, sV in synapses.items():
            if sK[1] == name:
                presNeuronV = neurons[sK[0]].Get_Value()
                weight = sV.Get_Weight()
                self.Presynaptic_Influence(presNeuronV, weight)
        self.Threshold()


    def Presynaptic_Influence(self, neuron, weight):
        self.Add_To_Value(neuron * weight)


# -------------------------- Private methods -------------------------

    def Determine_Name(self,line):
        if "name" in line:
            splitLine = line.split('"')
            self.name = splitLine[1]

    def Determine_Type(self,line):
        if "sensor" in line:
            self.type = const.SENSOR_NEURON

        elif "motor" in line:
            self.type = const.MOTOR_NEURON

        else:
            self.type = const.HIDDEN_NEURON

    def Print_Name(self):
       print(self.name)

    def Print_Type(self):
       print(self.type)

    def Print_Value(self):
       print(self.value , " " , end="" )

    def Search_For_Joint_Name(self, line):
        if "jointName" in line:
            splitLine = line.split('"')
            self.jointName = splitLine[5]

    def Search_For_Link_Name(self, line):
        if "linkName" in line:
            splitLine = line.split('"')
            self.linkName = splitLine[5]

    def Threshold(self):
        self.value = math.tanh(self.value)
