import sys, string
import com.xhaus.jyson.JysonCodec as json
from genymotionCloud.gmtool import Gmtool


if device_name is None:
    print "Please specify a name for the device."
    sys.exit(1)

action = Gmtool()
action.stop_device(device_name)
