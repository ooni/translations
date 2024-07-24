# utils.sh
function validate_app_param() {
    local app=$1
    if [[ "$app" != "probe-mobile" && "$app" != "news-media-scan" ]]; then
        echo "Invalid parameter. The app parameter should be either 'probe-mobile' or 'news-media-scan'."
        exit 1
    fi
}
