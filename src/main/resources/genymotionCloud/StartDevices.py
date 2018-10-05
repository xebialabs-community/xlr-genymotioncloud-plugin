import sys, string
import com.xhaus.jyson.JysonCodec as json
from genymotionCloud.gmtool import Gmtool


if template_name is None:
    print "Please specify a template name."
    sys.exit(1)

if device_name is None:
    print "Please specify a name for the device."
    sys.exit(1)

action = Gmtool()
print GenymotionCloudAccount['username']
print GenymotionCloudAccount['password']

action.connect(GenymotionCloudAccount['username'],GenymotionCloudAccount['password'])
action.register_license(GenymotionCloudAccount['license_key'])

if adb_serial_port:
    action.start_device(template_name, device_name, adb_serial_port)
else:
    action.start_device(template_name, device_name)

