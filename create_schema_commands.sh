export PYTHONPATH="${PWD}/..:${PWD}/../..:"

THREADS=10

# Disable multithreading in all numerical packages
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1


python3 \
    ./pipelines/create_schema_commands.py \
    --threads=${THREADS} \
    --data_location=$1 \
    $2


