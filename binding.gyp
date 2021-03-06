{
  "targets": [
    {
      "target_name": "rrdjs_bindings",
      "sources": [
        "src/rrdjs.cc",
        "src/rrdjs_info.cc",
        "src/rrdjs_fetch.cc",
        "src/rrdjs_create.cc",
        "src/rrdjs_update.cc",
        "rrdtool/src/rrd_hw.c",
        "rrdtool/src/hash_32.c",
        "rrdtool/src/rrd_diff.c",
        "rrdtool/src/rrd_open.c",
        "rrdtool/src/rrd_info.c",
        "rrdtool/src/rrd_fetch.c",
        "rrdtool/src/rrd_utils.c",
        "rrdtool/src/rrd_error.c",
        "rrdtool/src/rrd_update.c",
        "rrdtool/src/rrd_create.c",
        "rrdtool/src/rrd_format.c",
        "rrdtool/src/rrd_hw_math.c",
        "rrdtool/src/rrd_nan_inf.c",
        "rrdtool/src/rrd_rpncalc.c",
        "rrdtool/src/rrd_thread_safe.c",
      ],
      'defines': [
        'HAVE_CONFIG_H'
      ],
      'cflags': [
      ],
      'ldflags': [
      ],
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'libraries': [
      ],
      'xcode_settings': {
      },
    }
  ]
}
