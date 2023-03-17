export CUDA_VISIBLE_DEVICES="4,5,6,7"
python run_swag.py \
--model_name_or_path roberta-base \
--do_train \
--do_eval \
--learning_rate 5e-5 \
--num_train_epochs 1 \
--output_dir ./log \
--per_gpu_eval_batch_size=12 \
--per_device_train_batch_size=12 \
--overwrite_output \
--logging_strategy="steps" \
--logging_steps=500