
class Config:
    evristics = {  
      '.m':[  
         'Loc *\( *@\"(.*?)\" *\)',
         'NSLocalizedString *\( *@\"(.*?)\" *, *.*\)',
         'setTitle: *@\"(.*?)\"',
         '.title *= *@\"(.*?)\"'
      ],
      '.mm':[  
         'Loc *\( *@\"(.*?)\" *\)',
         'NSLocalizedString *\( *@\"(.*?)\" *, *.*\)',
         'setTitle: *@\"(.*?)\"',
         '.title *= *@\"(.*?)\"'
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
      'ZZZ'
   ]
    excluded_folders = ['Pods', '.git', 'Build']
    allowed_formats = ['.m', '.mm', '.storyboard', '.xib', '.strings', '.plist']
    