import typing

from discord.ext import commands


class IsNotSlashCommand(commands.CheckFailure):
    """
    The generic error for the bot failing the :func:`utils.checks.is_slash_command` check.
    """


def is_slash_command():
    """
    The check for whether or not the command is being used in a slash command (as defined by `ctx` being an instance of :class:`discord.ext.commands.SlashContext`).

    Raises:
        `IsNotSlashCommand`: If the command isn't being used in a slash command.
    """

    async def predicate(ctx: typing.Union[commands.Context, commands.SlashContext]):
        if isinstance(ctx.bot, commands.SlashContext):
            return True
        raise IsNotSlashCommand()

    return commands.check(predicate)
