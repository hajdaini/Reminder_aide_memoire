if test -f /etc/profile.d/git-sdk.sh
then
	TITLEPREFIX=SDK-${MSYSTEM#MINGW}
else
	TITLEPREFIX=$MSYSTEM
fi

if test -f ~/.config/git/git-prompt.sh
then
	. ~/.config/git/git-prompt.sh
else
	PS1='\[\033]0;$TITLEPREFIX:$PWD\007\]' # set window title
	PS1="$PS1"'\n'                 

	PS1="$PS1"'\[\033[01;31m\]'       # light red
	PS1="$PS1"'\u'             # user
	PS1="$PS1"'\[\033[37m\]'       # white
	PS1="$PS1"'@'                  # user
	PS1="$PS1"'\[\033[01;33m\]'       # light yellow
	PS1="$PS1"'\h '                 # host

	random_face_array[0]="(╬ ಠ益ಠ)"
	random_face_array[1]="(ಠ_ಠ)"
	random_face_array[2]="(｡◕‿◕｡)"
	random_face_array[3]="¯\_(ツ)_/¯"
	random_face_array[5]="ᕦ(ò_óˇ)ᕤ"
	random_face_array[6]="(づ｡◕‿‿◕｡)づ"
	random_face_array[7]="乁( ◔ ౪◔)「"
	random_face_array[8]="┑(￣Д ￣)┍"
	random_face_array[9]="( ͡ಠ ʖ̯ ͡ಠ)"
	random_face_array[10]="(っ▀¯▀)つ"
	random_face_array[11]="ʕʘ̅͜ʘ̅ʔ"	
	size=${#random_face_array[@]}

	PS1="$PS1"'\[\033[00;36m\]'      # cyan
	index=$(($RANDOM % $size))
	PS1="$PS1"'${random_face_array[$index]} '

	PS1="$PS1"'\[\033[37m\]'       # white
	PS1="$PS1"': '

	PS1="$PS1"'\[\033[01;34m\]'       # blu
	PS1="$PS1"'\w'                 # current working directory


	if test -z "$WINELOADERNOEXEC"
	then
		GIT_EXEC_PATH="$(git --exec-path 2>/dev/null)"
		COMPLETION_PATH="${GIT_EXEC_PATH%/libexec/git-core}"
		COMPLETION_PATH="${COMPLETION_PATH%/lib/git-core}"
		COMPLETION_PATH="$COMPLETION_PATH/share/git/completion"
		if test -f "$COMPLETION_PATH/git-prompt.sh"
		then
			. "$COMPLETION_PATH/git-completion.bash"
			. "$COMPLETION_PATH/git-prompt.sh"
			PS1="$PS1"'\[\033[01;32m\]'  # change color to cyan
			PS1="$PS1"'`__git_ps1`'   # bash function
		fi
	fi
	PS1="$PS1"'\[\033[01;31m\]'        # change color
	PS1="$PS1"'\n'                 # new line
	PS1="$PS1"' > '                 # prompt: always $
	PS1="$PS1"'\[\033[37m\]'       # yellow

fi

MSYS2_PS1="$PS1"               # for detection by MSYS2 SDK's bash.basrc
