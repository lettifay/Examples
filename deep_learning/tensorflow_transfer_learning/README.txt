https://www.tensorflow.org/tutorials/image_retraining

1. env setup
source /opt/DL/tensorflow/bin/tensorflow-activate
git clone https://github.com/tensorflow/tensorflow.git

2. transfer learning based on ImageNet model
python /home/crf/tf_transfer_learning/retrain.py \
--how_many_training_steps 2000 \
--train_batch_size 64 \
--validation_batch_size 2 \
--learning_rate 0.01 \
--testing_percentage 10 \
--validation_percentage 10 \
--eval_step_interval 10 \
--final_tensor_name final_result \
--summaries_dir /home/crf/tf_transfer_learning/retrain_logs \
--output_labels /home/crf/tf_transfer_learning/output_labels.txt \
--output_graph /home/crf/tf_transfer_learning/output_graph.pb \
--image_dir /home/crf/tf_transfer_learning/dolphins-and-seahorses/train_val \
--model_dir /home/crf/tf_transfer_learning/imagenet \
--bottleneck_dir /home/crf/tf_transfer_learning/bottleneck \
--print_misclassified_test_images True \
--architecture inception_v3

3. check info in tensorboard
tensorboard --logdir /home/crf/tf_transfer_learning/retrain_logs

4. inference
python /home/crf/tf_transfer_learning/label_image.py \
--graph=/home/crf/tf_transfer_learning/output_graph.pb \
--labels=/home/crf/tf_transfer_learning/output_labels.txt \
--input_layer=DecodeJpeg/contents:0 \
--output_layer=final_result:0 \
--num_top_predictions 5 \
--image=/home/crf/tf_transfer_learning/dolphins-and-seahorses/test/dolphin2.jpg

5. just get image bottleneck
python /home/crf/tf_transfer_learning/get_bottleneck.py \
--image_dir /home/crf/tf_transfer_learning/dolphins-and-seahorses/train_val \
--model_dir /home/crf/tf_transfer_learning/imagenet \
--summaries_dir /home/crf/tf_transfer_learning/retrain_logs \
--bottleneck_dir /home/crf/tf_transfer_learning/bottleneck \
--architecture inception_v3
