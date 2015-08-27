
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
      '.swift':[
          'NSLocalizedString\(\"(.*?)\",'
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
      '.swift':[
          '\"(.*?)\"'
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
      '^[0-9]+$',
      '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
      '!=',
      '(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?',
      '\(null\)',
      '\[view\]',
      '#subscriptions',
      '%@',
      '<=',
      '==',
      '>=',
      'dd/MM',
      'HH:mm',
      'id',
      'NetworkRequest not responds to selector parameters',
      'V:\[',
      'yyyy',
      'ZZZ'
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
    allowed_formats = ['.m', '.mm', '.swift', '.storyboard', '.xib', '.strings', '.plist']


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