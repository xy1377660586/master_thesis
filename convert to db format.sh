DATA=myfinetunning/data
echo 'create train lmdb'
rm -rf $DATA/img_train_lmdb
build/tools/convert_imageset --shuffle / $DATA/train.txt  $DATA/img_train_lmdb

echo 'creat test lmdb'
rm -rf $DATA/img_test_lmdb
build/tools/convert_imageset --shuffle / $DATA/test.txt  $DATA/img_test_lmdb

echo 'Done..'
