#!/bin/bash
set -eo pipefail

rm -rf dist
echo "Installing dependencies"
pip3 install --target ./dist -r requirements.txt

echo "Running tests..."
pytest

echo "Zipping..."
cp -r ./src ./dist/
cp version.properties ./dist/
cd dist
zip -r app.zip .

echo "Done!"


# optional - uploads zip to s3
version=`cat version.properties`
#echo "Uploading App Version: $version to S3..."
#aws s3 cp dist/app.ziip s3://app-storage/app1/${version}/app.zip

