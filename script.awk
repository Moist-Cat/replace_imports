{ if ($1 == "import" || $1 == "from" || $0 == "")
      # doesn't catch from foo.bar import target
      # that's OK
      split($2, qualname, ".");
      a = qualname[1]
      if (qualname[1] == target) {
          gsub(target, repl)
      };
  print($0)
}
