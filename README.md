# Artificial Neural Network Regressor to Predict Rate of Penetration during Oil Well Drilling Operation


# Table of content

1. [Project Overview](#1)
2. [Understanding the Data](#2)
3. [Traditional Machine Learning Algorithms to Predict ROP](#3)
4. [Deep learning (Neural Network) Regressor to Predict ROP](#4)
5. [References](#5)


<a name="1"></a>
# Project Overview
In this project, artificial neural networks were used to predict rate of penetration (ROP), also called drill rate (DR), during an oil well drilling operation. The Volve datasets, published by Equinor in 2018 (on a license of Creative Commons BY-NC-SA 4.0), were used to build the deep learning model. This dataset belongs to the Volve field located off
the coast of Norway, which was preprocessed by Tunkiel et al. (Tunkiel et al., 2020) to convert the real-time drilling logs from segmented WITSML files into compact CSV files. This dataset is publicly available and can be accessed through University of Stavanger website. It contains the data of 7 wells with the following 12 commonly logged attributes:

* Measured Depth 
* Weight on Bit
* Average Standpipe Pressure
* Average Surface Torque
* Rate of Penetration
* Average Rotary Speed
* Mud Flow
* Mud Density
* Diameter
* Average Hookload
* Hole Depth (TVD) 
* University of Stavanger Rate of Penetration (USROP) Gamma 

The following 7 wells' datasets were used in this project:
 
* Norway-NA-15_$47$_9-F-9 A depth
* Norway-Statoil-15_$47$_9-F-7 depth
* Norway-StatoilHydro-15_$47$_9-F-14 depth
* Norway-StatoilHydro-15_$47$_9-F-15 depth
* Norway-StatoilHydro-15_$47$_9-F-15S depth
* Norway-StatoilHydro-15_$47$_9-F-5 depth
* Norway-StatoilHydro-15_$47$_9-F-9 depth

<a name="2"></a>
# Understanding the Data

Various attributes of the first well, Norway-NA-15_$47$_9-F-9 A depth, were presented in Fig. 1.

![final_2data](https://user-images.githubusercontent.com/54812742/139796959-bdff912e-c9ab-484c-98b1-7a12eba2b201.PNG)

Fig. 1: Distribution of different attributes for well "Norway-NA-15_$47$_9-F-9 A depth"

The Mud density and average hookload for this well were reported as 1.21 ± 0.01 gr/cm3 and 92.71 ± 4.40 kkgf, respectively. 

<a name="3"></a>
# Traditional Machine Learning Algorithms to Predict ROP
These datasets were previously used by Tunkiel et al. (Tunkiel et al., 2021) to predict ROP through traditional machine learning (ML) algorithms such as
 
* Gradient Boosting
* Random Forest
* AdaBoost
* KNeighbors

One of the metrics suggested to evaluate the ROP prediction model is Mean Absolute Error (MAE). The results are compared in Fig. 2 (Tunkiel et al., 2021). As shown, Gradient Boosting delivers the best results in terms of MAE.

![3](https://user-images.githubusercontent.com/54812742/139908038-4f400671-5130-4466-bcdf-bb0ff6bec372.png)

Fig. 2: ROP MAE obtained for various traditional machine learning algorithms 

In this project, the same datasets as used by Tunkiel et al. (Tunkiel et al., 2021) were used to build the deep learning model and finally, the results are compared with the results of the mentioned traditional ML algorithms.  

<a name="4"></a>
# Deep learning (Neural Network) Regressor to Predict ROP

A neural network with two dense layers of **relu** as activation function was trained. Mean squared error, adam optimizer, and mean absolute error were chosen as loss function, optimizer, and metrics, respectively. The loss and accuracy vs. number of epochs for the training and validation datasets are shown in Fig. 3. 

![final](https://user-images.githubusercontent.com/54812742/139790980-e58aee5b-5ae5-4df5-b88f-f8efeda0a4ca.PNG)

Fig. 3: (a) Accuracy and (b) loss for the training and validation datasets vs. number of epochs

The predicted rate of penetration (ROP) values were compared with the ground truth ones in Fig. 4.

![PRED1](https://user-images.githubusercontent.com/54812742/139910230-7b43a026-1197-4df2-ba64-d29420032129.PNG)

Fig. 4: Comparison of the predicted ROP from Neural Network Model with the ground truth values

The MAE obtained through deep learning model is **1.8**, which is much less than the value obtained through the best traditional machine learning algorithm with 10.73 as MAE (i.e., Gradient Boosting (Fig. 2)). This is a remarkable improvement verifying the fact that the deep learning algorithms can significantly surpass the traditional machine learning algorithms when there is a huge amount of data available, which is the case when it comes to drilling datasets. 

<a name="5"></a>
# References 

Equinor (2018). Volve field data (CC BY-NC-SA 4.0). https://www.equinor.com/en/news/14jun2018-disclosing-volve-data.html.

Tunkiel, A.,  Sui, D., Wiktorski, T. (2021). Reference dataset for rate of penetration benchmarking, Journal of Petroleum Science and Engineering, 196, 108069. 

Tunkiel, A.T., Wiktorski, T., Sui, D. (2020). Drilling dataset exploration, processing and interpretation using Volve field data. In: Submitted to Proceedings of the International Conference on Offshore Mechanics and Arctic Engineering - OMAE.
