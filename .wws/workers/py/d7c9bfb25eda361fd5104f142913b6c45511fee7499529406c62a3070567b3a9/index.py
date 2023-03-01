from poly import *

"""
This module provides the base definition for patterns.
"""

import dataclasses
import re
import warnings
from typing import (
	Any,
	AnyStr,
	Iterable,
	Iterator,
	Match as MatchHint,
	Optional,
	Pattern as PatternHint,
	Tuple,
	Union)


class Pattern(object):
	"""
	The :class:`Pattern` class is the abstract definition of a pattern.
	"""

	# Make the class dict-less.
	__slots__ = ('include',)

	def __init__(self, include: Optional[bool]) -> None:
		"""
		Initializes the :class:`Pattern` instance.

		*include* (:class:`bool` or :data:`None`) is whether the matched
		files should be included (:data:`True`), excluded (:data:`False`),
		or is a null-operation (:data:`None`).
		"""

		self.include = include
		"""
		*include* (:class:`bool` or :data:`None`) is whether the matched
		files should be included (:data:`True`), excluded (:data:`False`),
		or is a null-operation (:data:`None`).
		"""

	def match(self, files: Iterable[str]) -> Iterator[str]:
		"""
		DEPRECATED: This method is no longer used and has been replaced by
		:meth:`.match_file`. Use the :meth:`.match_file` method with a loop
		for similar results.

		Matches this pattern against the specified files.

		*files* (:class:`~collections.abc.Iterable` of :class:`str`)
		contains each file relative to the root directory (e.g.,
		:data:`"relative/path/to/file"`).

		Returns an :class:`~collections.abc.Iterable` yielding each matched
		file path (:class:`str`).
		"""
		warnings.warn((
			"{0.__module__}.{0.__qualname__}.match() is deprecated. Use "
			"{0.__module__}.{0.__qualname__}.match_file() with a loop for "
			"similar results."
		).format(self.__class__), DeprecationWarning, stacklevel=2)

		for file in files:
			if self.match_file(file) is not None:
				yield file

	def match_file(self, file: str) -> Optional[Any]:
		"""
		Matches this pattern against the specified file.

		*file* (:class:`str`) is the normalized file path to match against.

		Returns the match result if *file* matched; otherwise, :data:`None`.
		"""
		raise NotImplementedError((
			"{0.__module__}.{0.__qualname__} must override match_file()."
		).format(self.__class__))


class RegexPattern(Pattern):
	"""
	The :class:`RegexPattern` class is an implementation of a pattern
	using regular expressions.
	"""

	# Keep the class dict-less.
	__slots__ = ('regex',)

	def __init__(
		self,
		pattern: Union[AnyStr, PatternHint],
		include: Optional[bool] = None,
	) -> None:
		"""
		Initializes the :class:`RegexPattern` instance.

		*pattern* (:class:`str`, :class:`bytes`, :class:`re.Pattern`, or
		:data:`None`) is the pattern to compile into a regular expression.

		*include* (:class:`bool` or :data:`None`) must be :data:`None`
		unless *pattern* is a precompiled regular expression (:class:`re.Pattern`)
		in which case it is whether matched files should be included
		(:data:`True`), excluded (:data:`False`), or is a null operation
		(:data:`None`).

			.. NOTE:: Subclasses do not need to support the *include*
			   parameter.
		"""

		if isinstance(pattern, (str, bytes)):
			assert include is None, (
				"include:{!r} must be null when pattern:{!r} is a string."
			).format(include, pattern)
			regex, include = self.pattern_to_regex(pattern)
			# NOTE: Make sure to allow a null regular expression to be
			# returned for a null-operation.
			if include is not None:
				regex = re.compile(regex)

		elif pattern is not None and hasattr(pattern, 'match'):
			# Assume pattern is a precompiled regular expression.
			# - NOTE: Used specified *include*.
			regex = pattern

		elif pattern is None:
			# NOTE: Make sure to allow a null pattern to be passed for a
			# null-operation.
			assert include is None, (
				"include:{!r} must be null when pattern:{!r} is null."
			).format(include, pattern)

		else:
			raise TypeError("pattern:{!r} is not a string, re.Pattern, or None.".format(pattern))

		super(RegexPattern, self).__init__(include)

		self.regex: PatternHint = regex
		"""
		*regex* (:class:`re.Pattern`) is the regular expression for the
		pattern.
		"""

	def __eq__(self, other: 'RegexPattern') -> bool:
		"""
		Tests the equality of this regex pattern with *other* (:class:`RegexPattern`)
		by comparing their :attr:`~Pattern.include` and :attr:`~RegexPattern.regex`
		attributes.
		"""
		if isinstance(other, RegexPattern):
			return self.include == other.include and self.regex == other.regex
		else:
			return NotImplemented

	def match_file(self, file: str) -> Optional['RegexMatchResult']:
		"""
		Matches this pattern against the specified file.

		*file* (:class:`str`)
		contains each file relative to the root directory (e.g., "relative/path/to/file").

		Returns the match result (:class:`RegexMatchResult`) if *file*
		matched; otherwise, :data:`None`.
		"""
		if self.include is not None:
			match = self.regex.match(file)
			if match is not None:
				return RegexMatchResult(match)

		return None

	@classmethod
	def pattern_to_regex(cls, pattern: str) -> Tuple[str, bool]:
		"""
		Convert the pattern into an uncompiled regular expression.

		*pattern* (:class:`str`) is the pattern to convert into a regular
		expression.

		Returns the uncompiled regular expression (:class:`str` or :data:`None`),
		and whether matched files should be included (:data:`True`),
		excluded (:data:`False`), or is a null-operation (:data:`None`).

			.. NOTE:: The default implementation simply returns *pattern* and
			   :data:`True`.
		"""
		return pattern, True


@dataclasses.dataclass()
class RegexMatchResult(object):
	"""
	The :class:`RegexMatchResult` data class is used to return information
	about the matched regular expression.
	"""

	# Keep the class dict-less.
	__slots__ = (
		'match',
	)

	match: MatchHint
	"""
	*match* (:class:`re.Match`) is the regex match result.
	"""


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
