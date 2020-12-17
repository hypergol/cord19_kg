export PYTHONPATH="${PWD}/..:${PWD}/../..:"

THREADS=30

# Disable multithreading in all numerical packages
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1

python3 \
    ./pipelines/create_schema.py \
    --threads=${THREADS} \
    --data_directory=$1 \
    --raw_data_location=$2 \
    $3
