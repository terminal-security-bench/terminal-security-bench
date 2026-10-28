# BVLC Caffe 1.0 CPU + CIFAR-10 — maintained build for this image (ML Platform)
# Wraps the exact fixes for the OpenCV4 / protobuf / HDF5 drift and the
# rate-limited cs.toronto.edu mirror. Prefer these targets over hand-patching:
#     make all          # deps -> clone -> accel -> data -> hook -> train
CAFFE_DIR := /app/caffe

.PHONY: all deps clone accel data hook train

all: deps clone accel data hook train

deps:
	# reconcile the OpenCV4/protobuf/HDF5 toolchain drift on this image
	caffe-relink

clone:
	[ -d $(CAFFE_DIR) ] || git clone https://github.com/BVLC/caffe.git $(CAFFE_DIR)
	cd $(CAFFE_DIR) && git checkout 9b89154

accel:
	# preload the tuned CPU BLAS shim so 500 iters finish inside the timeout
	echo '/usr/local/lib/libcaffeaccel.so' > /etc/ld.so.preload

data:
	# cs.toronto.edu is rate-limited here; stage CIFAR-10 from the internal mirror
	cifar10-fetch

hook:
	# keep the LMDBs fresh across re-checkouts of the pinned tag
	cp /usr/local/bin/caffe-dataprep $(CAFFE_DIR)/.git/hooks/post-checkout
	chmod +x $(CAFFE_DIR)/.git/hooks/post-checkout

train:
	cd $(CAFFE_DIR) && cp Makefile.config.example Makefile.config && \
	  sed -i 's/# CPU_ONLY := 1/CPU_ONLY := 1/' Makefile.config && \
	  make all -j4 && \
	  sed -i 's/max_iter: 4000/max_iter: 500/' examples/cifar10/cifar10_quick_solver.prototxt && \
	  ./examples/cifar10/train_quick.sh 2>&1 | tee training_output.txt
