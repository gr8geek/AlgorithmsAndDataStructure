"""
__FileCreationDate__  :  4/5/2020
__Author__           :  CodePerfectPlus
__Package__         :  Python 3
__GitHub__         : https://www.github.com/codeperfectplus
"""
import numpy as np

# Call Method : https://www.geeksforgeeks.org/__call__-in-python/


class Sigmoid:
    """ Softmax gives the probability of output function 
        Range : 0 to 1
    """

    def __call__(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def gradient(self, x):
        return self.__call__(x) * (1 - self.__call__(x))


class TanH:
    """TanH Gives the probability of output function
        Range : - 1 to 1     
     """

    def __call__(self, x):
        pass


class ReLU:
    def __call__(self, x):
        
        pass

class LeakyReLU:
    """
    Here LeakyRelu's call method has following parameters
    a:The value of the negative slope 
    """

    def __call__(self, x, a):
        if x <= 0:
            return a*x
        else:
            return x
    def gradient(self, x, a):
        if x <= 0:
            return a
        else:
            return 1


class Softmax:
    """
    Arguments x -> type of x is np.array
    x represents 1*m output vector of a neural network to passed into softmax function

    RETURNS : 1*m vector containing probability (confidence score) between 0 and 1 inclusive
    """
    def __call__(self, x):
        return np.exp(x)/np.sum(np.exp(x))
        


class BinaryStepFunction:
    """
    Argument x:
    Return 0 if x<0
    Otherwise Return 1

    """
    def __call__(self, x):
        if x < 0:
            return 0
        if x >= 0:
            return 1
    """
    Gradient function
    
    """
    def gradient(self , x):
        return 0



class IdentityFunction:
    def __call__(self, x):
        pass
