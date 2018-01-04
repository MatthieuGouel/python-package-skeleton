if [ ! -z "$1" ]
then
    echo "Initialization of $1 project"
    ggrep -lri "skeleton" | xargs gsed -i "s/skeleton/$1/gI"
    mv skeleton $1
    echo "Success ! You can now delete new.sh (rm new.sh)"
fi
