# This file must be used with "source bin/activate.fish" *from fish*
# you cannot run it directly

function deactivate
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        set -gx PATH "$_OLD_VIRTUAL_PATH"
        set -e _OLD_VIRTUAL_PATH
    end

    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME "$_OLD_VIRTUAL_PYTHONHOME"
        set -e _OLD_VIRTUAL_PYTHONHOME
    end

    # unset VIRTUAL_ENV
    if test -n "$VIRTUAL_ENV"
        set -e VIRTUAL_ENV
    end

    # This should detect bash and zsh, which have a hash command that must
    # be called to get it to forget past commands.  Without forgetting
    # past commands the $PATH changes we made may not be respected
    if test -n "$BASH" -o -n "$ZSH_VERSION"
        hash -r
    end

    if test -n "$_OLD_VIRTUAL_PS1"
        set -gx PS1 "$_OLD_VIRTUAL_PS1"
        set -e _OLD_VIRTUAL_PS1
    end

if set -q VIRTUAL_ENV_DISABLE_PROMPT
    set -e -U VIRTUAL_ENV_DISABLE_PROMPT
end


    # Self destruct!
    functions -e deactivate
end

# unset irrelevant variables
deactivate nondestructive

set -gx VIRTUAL_ENV "/home/valium/Desktop/fertiliser/template"

set -gx _OLD_VIRTUAL_PATH "$PATH"
set -gx PATH "$VIRTUAL_ENV/bin" $PATH

# unset PYTHONHOME if set
# this will fail if PYTHONHOME is set to the empty string (which is bad anyway)
# could use `if (set -u; : $PYTHONHOME) ;` in bash
if test -n "$PYTHONHOME"
    set -gx _OLD_VIRTUAL_PYTHONHOME "$PYTHONHOME"
    set -e PYTHONHOME
end

set -gx VIRTUAL_ENV_DISABLE_PROMPT

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    set -gx _OLD_VIRTUAL_PS1 "$PS1"
    if test "x(template) " != "x"
        set -gx PS1 "(template) $PS1"
    else if test "(template)" != "__"
        # special case for Aspen magic directories
        # see https://aspen.io/
        set -gx PS1 "[ (basename (dirname $VIRTUAL_ENV)) ] $PS1"
    else
        set -gx PS1 "(basename $VIRTUAL_ENV) $PS1"
    end
    export PS1
end

# This should detect bash and zsh, which have a hash command that must
# be called to get it to forget past commands.  Without forgetting
# past commands the $PATH changes we made may not be respected
if test -n "$BASH" -o -n "$ZSH_VERSION"
    hash -r
end
