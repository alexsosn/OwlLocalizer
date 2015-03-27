
class Config:
    evristics = {  
      '.m':[  
         'Loc *\( *@\"(.*?)\" *\)',
         'NSLocalizedString *\( *@\"(.*?)\" *, *.*\)',
         'setTitle: *@\"(.*?)\"',
         '.title *= *@\"(.*?)\"',
         'alertMessage:@\"(.*?)\"'
      ],
      '.mm':[  
         'Loc *\( *@\"(.*?)\" *\)',
         'NSLocalizedString *\( *@\"(.*?)\" *, *.*\)',
         'setTitle: *@\"(.*?)\"',
         '.title *= *@\"(.*?)\"',
         'alertMessage:@\"(.*?)\"'
      ],
      '.xib':[  
         ' title=\"(.*?)\".*/>'
      ],
      '.storyboard':[  
         ' title=\"(.*?)\".*/>'
      ],
      '.strings':[  
         '\".*?\" *= *\"(.*?)\";'
      ],
      '.plist':[]
   }
    strings_patterns = {
      '.m':[  
         '@\"(.*?)\"'
      ],
      '.mm':[  
         '@\"(.*?)\"'
      ],
      '.xib':[  
         ' title=\"(.*?)\".*/>'
      ],
      '.storyboard':[  
         ' title=\"(.*?)\".*/>'
      ],
      '.strings':[  
         '\".*?\" *= *\"(.*?)\";'
      ],
      '.plist':[  
         '<string>(.*?)</string>'
      ]
   }
    excluded_patterns = [
      '(H|V):\|.*?\[.*\].*?\|',
      '(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?',
      '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
      '!=',
      '==',
      '>=',
      '<=',
      'yyyy',
      'ZZZ',
      '^[0-9]+$',
      '\[view\]',
      '\(null\)',
      'V:\[',
      'HH:mm',
      'dd/MM',
      '%@',
      'ok',
      'sort',
      'sort',
      'sort',
      'id',
      'state',
      'name',
      'sort',
      'id',
      'state',
      'id',
      'state',
      'id',
      'state',
      'name',
      'sort',
      'id',
      'state',
      'name',
      'sort',
      'indigo',
      'lime',
      'navy',
      'ivory',
      'green',
      'green yellow',
      'azure',
      'maroon',
      'yellow green',
      'value',
      'value',
      'value',
      'width',
      'validation',
      'validation',
      'validation',
      'validation',
      'validation',
      'icons',
      'type',
      'type',
      'name',
      'id',
      'state',
      'name',
      'value',
      'location',
      'type',
      'type',
      'id',
      'id',
      'id',
      'id',
      'value',
      'value',
      'value',
      'ok',
      'id',
      'type',
      'name',
      'value',
      'value',
      'value',
      'name',
      'longitude',
      'NetworkRequest not responds to selector parameters',
      'status',
      'error',
      'status',
      'errors',
      'status',
      'status',
      'type',
      'type',
      'value',
      'name',
      'text',
      'id',
      'status',
      'status',
      'status',
      'name',
      'html',
      '#subscriptions',
      'notifications',
      'identifier',
      'en',
      'sort',
      'id',
      'state',
      'name',
      'sort',
      'id',
      'state',
      'id',
      'state',
      'id',
      'state',
      'name',
      'sort',
      'id',
      'state',
      'name',
      'sort'
   ]
    excluded_lines = [
        'NSAssert\(.*?\)',
        'NSLog\(.*?\)',
        'DDLogError',
        'DDLogVerbose',
        'it\(@"',
        'ForKey:@"',
        'DLog\(@',
        'NSException'
    ]
    excluded_folders = ['Pods', '.git', 'Build']
    allowed_formats = ['.m', '.mm', '.storyboard', '.xib', '.strings', '.plist']


'''
Currently not rejected with NLTK:
dd/MM HH:mm
dd/MM hh:mm a
NSAssert(self.model != nil, @"Model not set");
DDLogError(@"failure error: %@", error);
DDLogVerbose(@"error object: %@", object);
#import <XCTest/XCTest.h>

...Spec.m
describe(@"Math", ^{
     it(@"is pretty cool", ^{
numberForKey:@"id"


Not included with heuristics:
[self alertMessage:@"An email will be sent to you shortly." withTitle:@"Reset password confirmation"];
[NSPredicate predicateWithFormat:@"identifier == %@"

'''