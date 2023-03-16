export CUDA_VISIBLE_DEVICES=""
python run_swag.py \
--model_name_or_path roberta-base \
--do_train \
--do_eval \
--learning_rate 5e-5 \
--num_train_epochs 3 \
--output_dir /tmp/swag_base \
--per_gpu_eval_batch_size=1 \
--per_device_train_batch_size=1 \
--overwrite_output