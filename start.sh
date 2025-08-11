#!/bin/bash
set -e

# 讀取 MySQL 設定
MYSQL_VERSION=$(grep MYSQL_VERSION .env | cut -d '=' -f2)
MYSQL_PORT=$(grep MYSQL_PORT .env | cut -d '=' -f2)
MYSQL_ROOT_PASSWORD=$(grep MYSQL_ROOT_PASSWORD .env | cut -d '=' -f2)

# 如果是 latest，就查實際版本
if [ "$MYSQL_VERSION" = "latest" ]; then
    echo "🔍 正在檢查 MySQL latest 實際版本..."
    docker pull mysql:latest > /dev/null
    ACTUAL_VERSION=$(docker image inspect mysql:latest --format '{{index .RepoTags 0}}')
    echo "✅ MySQL latest 目前對應版本：$ACTUAL_VERSION"
fi

# 啟動容器
echo "🚀 啟動 docker-compose..."
docker compose up -d

# 檢查 MySQL 啟動狀態（最多 30 秒）
echo "⏳ 等待 MySQL 啟動中..."
for i in {1..30}; do
    if docker exec $(grep MYSQL_CONTAINER_NAME .env | cut -d '=' -f2) \
        mysqladmin ping -h "127.0.0.1" -P 3306 -p"${MYSQL_ROOT_PASSWORD}" --silent; then
        echo "✅ MySQL 已成功啟動並可連線！"
        exit 0
    fi
    sleep 1
done

echo "❌ MySQL 啟動逾時或連線失敗，請檢查容器日誌："
docker logs $(grep MYSQL_CONTAINER_NAME .env | cut -d '=' -f2)
exit 1