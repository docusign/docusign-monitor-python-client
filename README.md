# The Official DocuSign Monitor Python Client

[![PyPI version][pypi-image]][pypi-url]
<!--[![PyPI downloads][downloads-image]][downloads-url]-->
[![Build status][travis-image]][travis-url]

[PyPI module](https://pypi.python.org/pypi/docusign_monitor) that wraps the <a href="https://www.docusign.com/products/monitor-for-real-estate">DocuSign Monitor</a> API

[Documentation about the DocuSign Monitor API](https://developers.docusign.com/)

## Requirements

- Python 2.7 (3.7+ recommended)
- Free [Developer Sandbox](https://go.docusign.com/sandbox/productshot/?elqCampaignId=16531)

## Compatibility

- Python 2.7+

## Installation

### Path Setup:

1. Locate your Python installation, also referred to as a **site-packages** folder. This folder is usually labeled in a format of Python{VersionNumber}.

**Examples:**

- **Unix/Linux:** /usr/lib/python2.7
- **Mac:** /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7
- **Windows:** C:\Users\{username}\AppData\Local\Programs\Python\Python37

1. Add the path to your Python folder as an environment variable.

**Unix/Linux:**

- Type the following command into your console:  
   **export PYTHONPATH = "${PYTHONPATH}:.:/path/to/site-packages"**
- Optionally, you can add this command to your system profile, which will run the command each time Python is launched.

**Windows:**

<ol>
   <li>Open the Windows <b>Control Panel.</b></li>
   <li>Under the System and Security category, open the <b>System</b></li>
   <li>Select <b>Advanced System Settings</b> to open the <b>System Properties</b> dialog box.</li>
   <li>On the <b>Advanced</b> tab, select the <b>Environmental Variables</b> button at the lower-right corner.
       <ol style="list-style-type: lower-alpha">
           <li>Check if <b>PYTHONPATH</b> has been added as a <b>system variable.</b></li>
           <li>If it has not, select <b>New</b> to add it. The variable you add is the path to the <b>site-packages</b></li>
       </ol>
   </li>
</ol>

**Note:** If you are still unable to reference python or pip via your command console,you can also add the path to the site-packages folder to the built-in environment variable labeled **Path** , which will take effect the next time you start your machine.

### Install via PIP:

1. In your command console, type:
pip install docusign-monitor

Note: This may require the command console be elevated. You can accomplish this via sudoin Unix/Linux, or by running the command console as an administrator in Windows.

## Dependencies

This client has the following external dependencies:

- certifi v14.05.14+
- six v1.8.0+
- python\_dateutil v2.5.3+
- setuptools v21.0.0+
- urllib3 v1.15.1+
- jwcrypto v0.4.2+
- py-oauth2 v0.0.10+


## Support

Log issues against this client through GitHub. We also have an [active developer community on Stack Overflow](https://stackoverflow.com/questions/tagged/docusignapi).

## License

The DocuSign Python Client is licensed under the [MIT License](https://github.com/docusign/docusign-python-client/blob/master/LICENSE).


[pypi-image]: https://img.shields.io/pypi/v/docusign_monitor.svg?style=flat
[pypi-url]: https://pypi.python.org/pypi/docusign_monitor
[downloads-image]: https://img.shields.io/pypi/dm/docusign_monitor.svg?style=flat
[downloads-url]: https://pypi.python.org/pypi/docusign_monitor
[travis-image]: https://img.shields.io/travis/docusign/docusign-monitor-python-client.svg?style=flat
[travis-url]: https://travis-ci.org/docusign/docusign-monitor-python-client
