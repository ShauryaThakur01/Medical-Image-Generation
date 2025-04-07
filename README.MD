**Unpaired Medical Image Translation and Detection:- *Leveraging CycleGAN for Medical Image Generation with Brain Tumor Detection*** 

Shaurya Thakur (E21CSEU0580)

***Introduction*** 

Medical imaging is the foundation of modern diagnostic healthcare. It helps by providing critical insights into anatomical and pathological conditions of the subject. In the recent years, the field of medical imaging has been significantly influenced by the innovations in technology and primarily the Artificial Intelligence. Among various imaging techniques, Computed Tomography (CT) and Magnetic Resonance Imaging (MRI) are the one’s which are fundamentally used for diagnostic analysis and evaluation of various medical conditions. But both of these modalities have a unique advantages and challenges. CT scans are expeditious, cost-effective and widely available. But they have limited ability to resolve soft tissue contrast and leads to higher radiation exposure to patients. On the other hand, MRI delivers rich and detailed image without radiation exposure. But MRI scans are expensive and of longer acquisition times. This motivates the research into synthesizing CT scan images into MRI scan images and vice-versa using Generative AI which helps in enhancing diagnostic capabilities, reducing radiation exposure and lowering the expense. 

![](Aspose.Words.609e9d1a-251b-4860-a905-dac02a26fd65.001.jpeg)

*Fig 1: - Predicted and Actual values of brain tumor detection on various images.* 

Recent advancements in Artificial Intelligence, especially in Generative Adversarial Networks (GANs) have revolutionized the process of image synthesis and medical data augmentation. This research leverages “CycleGAN”, a deep learning framework for unpaired image-to-image synthesis. CycleGan enables bidirectional translation between two images without requiring paired datasets which implies the suitability for medical Imaging applications, in the cases where pairs are often not available. This means the model will be able to generate MRI images from CT scan images and vice- versa. In this model, to maintain structural fidelity, we are training two generators (one for CT to MRI and other one for MRI to CT conversion) and two corresponding discriminators. CycleGan enforces cycle consistency such that the generated image must maintain similar properties to its original image. Moreover, the integration of diagnostic verification related to Brain Tumor, into the pipeline further augments clinical utility of the generated images. 

![](Aspose.Words.609e9d1a-251b-4860-a905-dac02a26fd65.002.png) ![](Aspose.Words.609e9d1a-251b-4860-a905-dac02a26fd65.003.jpeg)

*Fig 2: - Image Generation from CT to MRI and vice versa* 

The aim of this project is to leverage CycleGAN for generating MRI to CT scan images and vice- versa due to the purpose of medical data augmentation and lowering radiation exposure while incorporating a diagnostic module like Brain Tumor detection to show the use case of the research.  

The generated images are evaluated both quantitively and qualitatively by using metrics such as the Structural Similarity Index Measure (SSIM) and Fréchet Inception Distance (FID). For instance, the SSIM is calculated using the below formula:-  

![](Aspose.Words.609e9d1a-251b-4860-a905-dac02a26fd65.004.png)

Where ‘ux’ and ‘uy’ are the averages of the images ‘x’ and ‘y’,  ‘sigma x ^ 2’ and ‘sigma y ^ 2’ are their variances and ‘sigma xy’ is the covariance and ‘c1’ & ‘c2’ are the constants to stabilize the division. 

To summarize the introduction, this research seeks to overcome the limitations of each modality by synthesizing MRI images to CT one’s which are not paired, thereby facilitating diagnostic accuracy while minimizing costs and radiation exposure.  

***Literature Review*** 

Over the years, image-to-image synthesis in medical imaging has witnessed several milestones. What is also known as Conditional Adversarial Networks, early works were applied on pix2pix, while the most recent efforts take advantage of unpaired translation techniques with no paired datasets required. 

**Image to Image translation with Conditional Adversarial Networks: -**  

The feasibility of pix2pix demonstrated the aspect of paired image translation where, the pix2pix uses a generator-discriminator architecture to map input image to its corresponding target domain while employing Conditional Adversarial Network (CAN). One of the major groundbreaking innovations in pix2pix was the use of L1 and L2 loss functions to the adversarial loss, which helps in tackling the deviations between synthesized and ground truth images. Furthermore, it uses skip connections to allow the network to preserve fine-grained details which are crucial for medical applications. However, the major limitation of pix2pix is that it can only work with paired data, which is often in most of the cases, expensive and hard to retrieve. This limitation motivates the exploration of unpaired translation methods.  

![](Aspose.Words.609e9d1a-251b-4860-a905-dac02a26fd65.005.png)

*Fig3:- pix2pix framework (Source:- ResearchGate)* 

Furthermore pCCGAN method offers several advantages over pix2pix. It eliminates the need for paired data, thus, significantly reducing the cost and challenges of data acquisition while maintaining high quality of image synthesis. However, pCCGAN training can be computationally expensive and requires large datasets for performance. 

![](Aspose.Words.609e9d1a-251b-4860-a905-dac02a26fd65.006.png)

*Fig4:- pCCGAN architecture (Source:- pCCGAN github repository)* 

**Unpaired Image Translation using CycleGAN:-**  

This GAN introduced the solution to the problem of paired-data which we were getting in Conditional Adversarial Networks(CAN) while working on pix2pix. CycleGAN makes sure that if an image is translated from one domain to the other then, it can be mapped back to its original form by enforcing a cyclic consistency loss. It works as a dual generator and discriminator architecture which has the applications for medical imaging when acquiring paired CT and MRI datasets is challenging. The cycle consistency loss is defined as:- 

![](Aspose.Words.609e9d1a-251b-4860-a905-dac02a26fd65.007.png)

The two generator (Gmri and Gct work in tandem with their respective discriminators. In the formula, x is an image source from the domain. This process ensures that the translation process preserves key details of the image.  

![](Aspose.Words.609e9d1a-251b-4860-a905-dac02a26fd65.008.jpeg)

*Fig5:- CycleGAN architecture (Source:- ResearchGate)* 

**Comparative Overview: -**  



|**Method** |Paired Data Requirement |Key Loss Functions |Strengths |Limitations |
| - | :- | - | - | - |
|Pix2pix |Yes |Adversarial + L1/L2 losses, Skip Connections |High-quality detail preservation |Requires paired datasets; may not generalize well |
|CycleGAN |No |Adversarial + Cycle Consistency Loss |Works with unpaired data; flexible architecture |Risk of mode collapse; turning of multiple losses |
|pCCGAN |No |<p>Adversarial + Forward- Backward cycle </p><p>+ Identity losses </p>|Enhanced stability; improved generalization |Computationally intensive; requires large datasets |

**Extensions for diagnostic Verification: -** 

Image translation constitutes one of the functions enabled by the integrated losses and modules which together enhance both diagnostic quality and image quality. Medical image generation and validation achieved optimal results through the use of a cycle perceptual loss that utilizes pretrained features between original and generated medical images. One such approach utilizes Brain Tumor Detection on generated images.  

![](Aspose.Words.609e9d1a-251b-4860-a905-dac02a26fd65.009.png)

*Fig6:- Brain Tumor Detection* 
