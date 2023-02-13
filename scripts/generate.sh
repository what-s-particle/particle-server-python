# Protobuf generates files in various languages, and configures them on demand.
# Protobuf Guideline https://go-kratos.dev/docs/guide/api-protobuf/
# For kotlin https://github.com/square/wire#generating-code-with-wire
# For swift  https://github.com/apple/swift-protobuf
# https://stackoverflow.com/questions/71091931/combine-every-single-protobuf-file-into-one-combined-proto

cd ../protos

PROTOC_INDIR=./pb_dir
PROTOC_OUTDIR=./build/123.proto

find $PROTOC_INDIR -type f -name "*.proto" | while read old_proto_file
do
  echo "// File: $PROTOC_INDIR" >> $PROTOC_OUTDIR
  cat $old_proto_file | \
    fgrep -v \
      -e 'import "' \
      -e 'package ' \
      -e 'syntax = "proto3";' \
    >> $PROTOC_OUTDIR
done


#protoc  --proto_path=./action --proto_path=./component --proto_path=./enum  --python_out=$PROTOC_OUTDIR  $(find . -iname '*.proto')
#sed -i $PROTOC_OUTDIR/*_pb2.py -e 's/^import [^ ]*_pb2/from . \0/'

#protoc --proto_path=. --swift_out=../merge/gen/swift $(find . -iname '*.proto')
#java -jar ./wire-compiler-4.5.0-jar-with-dependencies.jar --proto_path=. --android --kotlin_out=../merge/gen/kotlin  $(find . -iname '*.proto')



## generate proto code for all basedir
#python3 -m grpc_tools.protoc \
#    -I . \
#    --python_out=../particle/basedir \
#    ./action/addressbook_model.proto
##   $(find . -iname "*.proto")


#src_dir='basedir'
#dst_file='./123.proto'

# merge all pb files into one
#//protoc  --proto_path=./action --proto_path=./component --proto_path=./enum --descriptor_set_out=$dst_file ./action/*.proto ./component/*.proto ./enum/*.proto

#protoc  --python_out=$dst_file  --proto_path=$src_dir $(find . -iname '*.proto')
