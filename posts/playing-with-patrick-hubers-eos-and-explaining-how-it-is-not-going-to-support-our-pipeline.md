
.. title: Playing with Patrick Huber's EOS and explaining how it is not going to support our pipeline
.. slug: playing-with-patrick-hubers-eos-and-explaining-how-it-is-not-going-to-support-our-pipeline
.. date: 2018-03-01 17:22:30 UTC+05:30
.. tags: Research, 
.. category: 
.. link: 
.. description: 
.. type: text


Patrick's model is the only to truluy mention which has made the complete end to end process pipeline as opensource since this reconstruction of human faces has some market value as it has a capability to attract a good amount of people that might be the reason for less exposure of the code. Okay coming to partick's work it based on surrey model (University of Surrey).
It can be said it is most possible simplest pipeline for 2D-3D reconstruction of human face by simplest I mean relatively because it uses a linear techniques in order to estimate. So basically using some landmark detector we try to detect the landmarks where patrick's implementation supports 68 ones I personally prefer the ibug one. Using the landmark file we try to estiamte the camera parameters and try to minimize the error between the 2D landmarks and the projected 3D landmarks usually we come across this technique in Sfm technique and also other 3D reconstruciton pipeline because it is the heart of reconstruction. Using the camera parameters and the surrey's PCA model and the landmark points they to estiamte the shape parameters and project the image onto the 3D face. Patrick is still continuing his work by making the implementaion compatible with Basel Face Model & also trying to optimiza the parameters using Non linear implementations like Cerses Solver.
<!-- TEASER_END -->

The sample output will look like this 

