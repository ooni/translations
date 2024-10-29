app=${1:-"probe-mobile"}

echo $app

SUPPORTED_LANGUAGES=(ar ca de el es fa fr hi id is it nl pt_BR ro ru sw sk sq th tr zh_CN zh_TW my vi km)

if [ "$app" == "news-media-scan" ]; then
SUPPORTED_LANGUAGES=(fr de pt_BR ru es tr)
fi
