#!/usr/bin/env python
# coding: utf-8

# In[32]:


import math
import matplotlib.pyplot as plt

class Gaussian():
    """Gaussian distribution class for calculating and visualizing a Gaussian/Normal distribution.
    
    Attributes: 
    1. mean (float): representing the mean value of the distribution
    2. stdev (float): representing the standard deviation of the distribution
    3. data_list (list of floats): a list of floats extracted from the data file
    
    """
    
    def __init__(self, mu = 0, sigma = 1):
        self.mean = mu
        self.stdev = sigma
        self.data = []
    
    def calculate_mean(self):
        """Method for calcualating the mean of the data set
        
        Args: None
        
        Returns: float, mean of the data set
        
        """
        
        avg = 1.0*sum(self.data)/len(self.data)
        
        self.mean = avg
        return self.mean
    
    def calculate_stdev(self, sample=True):
        """ Method for calculating the standard deviation of the data set.
        
            Args: sample(bool); whether the data set represents a sample or population.
            
            Return: float, the standard deviation of the data set.        
        
        """
        
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
        
        mean = self.mean
        sigma = 0
        for d in self.data:
            sigma += (d-mean) **2
            
        sigma = math.sqrt(sigma/n)
        self.stdev = sigma
        return self.stdev
    
    def read_data_file(self, file_name, sample=True):
        """Method for reading data from a text file. The text file should have one float number per line.
        The numbers are stired in the data attribute. 
        The mean and standard deviation are calculated after the numbers have been read.
        
        Args:
            file_name: (string) the name of the file to read from.
            
        returns:
                none.
                   
        """
        
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
        
        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)
        
    def plot_histogram(self):
        
        """This method plots histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args: None
        
        Returns: None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')
        
    def pdf(self, x):
        
        """Method for calculating probability density function for the guassian distribution.
        
        Args: x(float) point for calculating the probability density function.
        
        Returns: Proability density fumction output.
        """
        
        return (1.0/(self.stdev*math.sqrt(2*math.pi))) * math.exp(-5.0*((x - self.mean) / self.stdev)**2)
    
    def plot_histogram_pdf(self, n_spaces = 50):
        
        """Method for plotting the normalized histogram of the data and 
        the plot of the pdf along the same range
        
        Args: n_spaces(int): Number of data points
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """
        
        mu = self.mean
        sigma = self.stdev
        
        min_range = min(self.data)
        max_range = max(self.data)
        
        #calculates the interval between x vakues
        interval = 1.0 * (max_range - min_range)/n_spaces
        
        x = []
        y = []
        
        #calculates the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))
            
        #make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')
        
        
        axes[1].plot(x, y)
        axes[1].set_title('Normal distribution for \n Sample mean and Standard deviation')
        axes[0].set_ylabel('Density')
        plt.show()
        
        return x, y
        
        
            


# In[33]:


gaussian_one = Gaussian()
gaussian_one.read_data_file('numbers.txt')


# In[34]:


print('The mean is {}'.format(gaussian_one.mean))
print('The standard deviation of the data is {}'.format(gaussian_one.stdev))


# In[35]:


gaussian_one.plot_histogram()


# In[36]:


gaussian_one.plot_histogram_pdf()


# In[ ]:





# In[ ]:





# In[ ]:




